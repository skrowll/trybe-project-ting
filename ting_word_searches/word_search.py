def exists_word(word, instance):
    queued = instance.queue
    occurrences = []

    for element in queued:
        for index in range(len(element["linhas_do_arquivo"])):
            if word.lower() in element["linhas_do_arquivo"][index].lower():
                occurrences.append({"linha": index + 1})
        if len(occurrences) > 0:
            return [{
                "palavra": word,
                "arquivo": element["nome_do_arquivo"],
                "ocorrencias": occurrences
                }]
        return []


def search_by_word(word, instance):
    queued = instance.queue
    occurrences = []

    for element in queued:
        for index in range(len(element["linhas_do_arquivo"])):
            if word.lower() in element["linhas_do_arquivo"][index].lower():
                occurrences.append({
                    "linha": index + 1,
                    "conteudo": element["linhas_do_arquivo"][index]
                    })
        if len(occurrences) > 0:
            return [{
                "palavra": word,
                "arquivo": element["nome_do_arquivo"],
                "ocorrencias": occurrences
                }]
        return []
