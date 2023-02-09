from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    files_names_list = []
    for element in instance.queue:
        files_names_list.append(element["nome_do_arquivo"])

    if path_file not in files_names_list:
        text_list = txt_importer(path_file)
        result_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_list),
            "linhas_do_arquivo": text_list
        }
        instance.enqueue(result_dict)
        print(result_dict, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        file_dequeued = instance.dequeue()
        path_file = file_dequeued["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        result_dict = instance.search(position)
        print(result_dict, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
