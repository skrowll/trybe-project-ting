from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_data = [
    {
        "nome_do_arquivo": "text_file_1.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["bla", "bla"]
    },
    {
        "nome_do_arquivo": "text_file_2.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["bla", "bla", "bla", "bla", "bla"]
    },
    {
        "nome_do_arquivo": "text_file_3.txt",
        "qtd_linhas": 8,
        "linhas_do_arquivo":
            ["bla", "bla", "bla", "bla", "bla", "bla", "bla", "bla"]
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(mock_data[0])
    priority_queue.enqueue(mock_data[1])
    priority_queue.enqueue(mock_data[2])

    assert len(priority_queue) == 3

    given = priority_queue.dequeue()
    assert len(priority_queue) == 2
    assert given == mock_data[0]
    given = priority_queue.dequeue()
    assert len(priority_queue) == 1
    assert given == mock_data[1]
    given = priority_queue.dequeue()
    assert len(priority_queue) == 0
    assert given == mock_data[2]

    priority_queue.enqueue(mock_data[0])
    priority_queue.enqueue(mock_data[1])
    priority_queue.enqueue(mock_data[2])

    assert priority_queue.search(0) == mock_data[0]
    assert priority_queue.search(1) == mock_data[1]
    assert priority_queue.search(2) == mock_data[2]

    priority_queue.dequeue()
    priority_queue.dequeue()
    priority_queue.dequeue()

    priority_queue.enqueue(mock_data[1])

    assert priority_queue.is_priority(mock_data[0]) is True
    assert priority_queue.is_priority(mock_data[2]) is False

    with pytest.raises(IndexError):
        priority_queue.search(10)
