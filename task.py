class TodositTask:
    def __init__(self, id, name, is_completed, priority, due, description, section_id) -> None:
        self.id = id
        self.name = name
        self.is_completed = is_completed
        self.priority = priority
        self.due = due
        self.description = description
        self.section_id = section_id

