import os
import shutil
import sys
import time


def copy_files(src, dst):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)

        # Рекурсивний виклик
        if os.path.isdir(src_path):
            copy_files(src_path, dst)
        else:
            # На випадок якщо розширення немає
            file_extension = os.path.splitext(item)[1][1:] or "other"
            # Створюємо директорію і копіюємо файл
            if file_extension:
                dest_dir = os.path.join(dst, file_extension)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy(src_path, dest_dir)


def main(src_dir, dst_dir):
 
    # Копіювання файлів
    try:
        copy_files(src_dir, dst_dir)
    except Exception as ex:
        print(f"Copy error: {ex}")
        time.sleep(20)
        sys.exit(1)

    print(f"Files successfully copied to {os.path.abspath(dst_dir)}")
    time.sleep(20)


if __name__ == "__main__":

    # Задаємо і перевіряємо вихідну директорію

    is_src_true = False

    while is_src_true == False:
        src_dir = input("The path of the source directory: ")
        if os.path.exists(src_dir):
            is_src_true = True
        else: print(f"Directory {src_dir} does not exist.")
            
    dst_dir = input("Destination directory path: ")
    # Cпроба створення директорії призначення, якщо її не існує
    try:
        os.makedirs(dst_dir, exist_ok=True)
    except Exception as ex:
        print(f"A default directory will be created")
    # Передаємо значення за замовчуванням
        dst_dir = "dist"

    main(src_dir, dst_dir)