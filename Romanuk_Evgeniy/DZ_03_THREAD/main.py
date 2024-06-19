import time
from ParseAndDownload import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing as mp


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        # Если папка уже существует, очищаем её содержимое
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Ошибка при удалении файла {file_path}: {e}")


def download_images_in_single_thread(urls, save_folder):
    create_directory(save_folder)

    start_time = time.time()
    for url in urls:
        download_image(url, save_folder)
    end_time = time.time()

    print(f"Загрузка с ипользованием одного потока завершена за {end_time - start_time} секунд")


def download_images_with_threads(urls, save_folder, num_threads):
    create_directory(save_folder)

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for url in urls:
            future = executor.submit(download_image, url, save_folder)
            futures.append(future)

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Exception during download: {e}")
    end_time = time.time()

    print(f"Загрузка с использованием {num_threads} потоков завершена за {end_time - start_time} секунд")


def download_images_with_processes(img_urls, save_folder, num_processes):
    create_directory(save_folder)
    start_time = time.time()

    with mp.Pool(processes=num_processes) as pool:
        for url in img_urls:
            pool.apply_async(download_image, args=(url, save_folder, ))
        pool.close()
        pool.join()

    end_time = time.time()
    print(f"Загрузка с использованием {num_processes} процессов завершена за {end_time - start_time} секунд")


if __name__ == "__main__":
    url = 'https://repack-byrutor.org/page/1/'
    save_folder_single_thread = 'downloaded_images_singlethread'
    save_folder_threads = 'downloaded_images_threads'
    save_folder_processes = 'downloaded_images_processes'
    num_threads = 12
    num_processes = 12

    img_urls = set()
    parse_images(url, img_urls, 1)

    if img_urls:
        print(f"Найдено {len(img_urls)} изображений для скачивания.")
        download_images_in_single_thread(img_urls, save_folder_single_thread)
        download_images_with_threads(img_urls, save_folder_threads, num_threads)
        download_images_with_processes(img_urls, save_folder_processes, num_processes)
    else:
        print("Не удалось получить список изображений.")
