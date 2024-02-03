import os
import shutil
import sys


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


def main():

    # В консоль: copy_and_sort.py source destination

    if len(sys.argv) < 2:
        print(f"No arguments passed")
        sys.exit(1)

    src_dir = sys.argv[1]

    # Створення вихідної директорії, якщо вона вказана, або за замавчуванням

    if len(sys.argv) > 2:
        dst_dir = sys.argv[2]
    else: dst_dir = "dist"

    # Перевірка існування вихідної директорії
    if os.path.exists(src_dir) == False:
        print(f"Directory {src_dir} does not exist.")
        sys.exit(1)

    # Cтворення директорії призначення, якщо її не існує
    try:
        os.makedirs(dst_dir, exist_ok=True)
    except Exception as ex:
        print(f"A default directory will be created")
 
    # Копіювання файлів
    try:
        copy_files(src_dir, dst_dir)
    except Exception as ex:
        print(f"Copy error: {ex}")
        sys.exit(1)

    print(f"Files successfully copied to {os.path.abspath(dst_dir)}")


if __name__ == "__main__":
    main()