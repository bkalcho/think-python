# Author: Bojan G. Kalicanin
# Date: 27-Oct-2016
# Write a function called sed that takes as arguments a pattern string,
# replacement string, and two filenames; it should read the first file
# and write the contents into the second file (creating it if
# necessary). If the pattern string appears anywhere in the file, it
# should be replaced with the replacement string.
# If an error occurs while opening, reading, writing or closing files,
# your program should catch the exception, print an error message, and
# exit.

def sed(pattern, replacement, file1, file2):
    """
    Read the first file, and write the contents into the second file.
    If the pattern string appears anywhere in the file, it should be
    replaced with the replacement string.
    """
    try:
        f_obj_read = open(file1, 'r')
        f_obj_write = open(file2, 'w')
        for line in f_obj_read.readlines():
            new_line = line.replace(pattern, replacement)
            f_obj_write.write(new_line)
        f_obj_read.close()
        f_obj_write.close()
    except:
        print("Error occured!")


if __name__ == "__main__":
    file1 = "art_of_war.txt"
    file2 = "art_of_war_edited.txt"
    pattern = "are"
    replacement = "was"
    sed(pattern, replacement, file1, file2)