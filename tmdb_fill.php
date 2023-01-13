<?php

error_reporting(E_ALL ^ E_WARNING ^ E_DEPRECATED ^ E_NOTICE);
define('DATALIFEENGINE', true);
define('ROOT_DIR', __DIR__);
define('ENGINE_DIR', ROOT_DIR . '/engine');

require_once ENGINE_DIR . '/classes/plugins.class.php';
require_once DLEPlugins::Check(ENGINE_DIR . '/modules/functions.php');

// Время ожидания ответа от API
const TIMEOUT = 5;

// Ключ API
const API_TOKEN = 'b156e6d24abe787bc067a873c04975';



function xfieldsDataSave(array $xfields): string
{
	$filecontents = [];
	foreach ($xfields as $name => $value) {
		if (trim($value) === '') continue;
		$name = str_replace("|", "&#124;", $name);
		$name = str_replace("\r\n", "__NEWL__", $name);
		$value = str_replace("|", "&#124;", $value);
		$value = str_replace("\r\n", "__NEWL__", $value);
		$filecontents[] = "$name|$value";
	}
	$filecontents = $filecontents ? join('||', $filecontents) : '';
	return $filecontents;
}

function getHttpContent(string $url): string
{
	$ch = curl_init($url);

	curl_setopt_array($ch, [
		CURLOPT_RETURNTRANSFER	=> true,
		CURLOPT_HEADER			=> false,
		CURLOPT_SSL_VERIFYPEER	=> false,
		CURLOPT_FOLLOWLOCATION	=> false,

		CURLOPT_CONNECTTIMEOUT	=> TIMEOUT,
		CURLOPT_TIMEOUT			=> TIMEOUT,
	]);

	$data = curl_exec($ch);
	curl_close($ch);
	return $data;
}

function getAllohaTmdbId(array $query): int
{
	$query['token'] = API_TOKEN;
	$contents = getHttpContent('https://api.alloha.tv/?' . http_build_query($query));
	$data = json_decode($contents, true);
	return (int)$data['data']['id_tmdb'];
}

function setLog(string $log): void
{
	file_put_contents(__DIR__ . '/tmdb_fill.log', date('Y-m-d H:i:s') . '    ' .  $log . PHP_EOL, LOCK_EX | FILE_APPEND);
}


exec('ps -aux', $process_list);
$process_id = 0;
foreach ($process_list as $row) {
	if (stripos($row, __FILE__) !== false) {
		$row = preg_replace('#\s+#', ' ', $row);
		$row = explode(' ', $row);
		$process_id = (int)$row[1];
	}
}


if ($_GET['start'] == 1) {
	$process_id || exec('php ' . __FILE__ . ' > /dev/null 2>&1 & echo $!', $id);
	echo 'Процесс успешно запущен, ID = ' . $id[0];
	die();
}

if (isset($argv)) {
	setLog('=== START ===');
	$sql = $db->query('SELECT id, xfields FROM ' . PREFIX . '_post WHERE xfields NOT LIKE "%tmdbid|%"');
	setLog('Found rows: ' . $db->num_rows());

	while ($row = $db->get_row($sql)) {
		$xfields = xfieldsdataload(stripslashes($row['xfields']));
		if ($xfields['tmdbid']) continue;

		$kinopoisk_id = (int)$xfields['kpid'];
		$tmdb_id = 0;

		if ($kinopoisk_id) {
			$tmdb_id = getAllohaTmdbId(['kp' => $kinopoisk_id]);
		} elseif ($xfields['imdbid']) {
			$tmdb_id = getAllohaTmdbId(['imdb' => $xfields['imdbid']]);
		} else {
			setLog($row['id'] . '	не заполнены поля kpid и imdbid');
		}

		if ($tmdb_id) {
			$xfields['tmdbid'] = $tmdb_id;
			setLog($row['id'] . '    TMDB = ' . $tmdb_id);
			$db->query(sprintf('UPDATE %s_post SET xfields = "%s" WHERE id = %d'
				, PREFIX
				, $db->safesql(xfieldsDataSave($xfields))
				, $row['id']
			));
		} else {
			setLog($row['id'] . '    Нет данных от API');
		}
	}

	setLog('=== END ===');
	die();
}

?>

<a href="<?= $_SERVER['PHP_SELF'] ?>?start=1">Запустить</a>
<?php if ($process_id): ?>
<br>Процесс уже запущен, ID = <?= $process_id ?>
<?php endif; ?>