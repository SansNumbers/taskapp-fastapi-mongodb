def individual_serial(task) -> dict:
    return {
        'id': str(task["_id"]),
        'name': task["name"],
        'text': task["text"],
        'complete': task["complete"]
    }


def list_serial(tasks) -> list:
    return [individual_serial(task) for task in tasks]
