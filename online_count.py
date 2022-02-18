def count_online(people_status):
    return len({key:status for key, status in people_status.items() if status == 'online'})