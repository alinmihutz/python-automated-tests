from core.worker.WorkItem import WorkItem


class WorkItemFactory(object):
    @staticmethod
    def create_work_item(test_name):
        work_item = WorkItem(test_name)
        work_item.load_external_resources()

        return work_item
