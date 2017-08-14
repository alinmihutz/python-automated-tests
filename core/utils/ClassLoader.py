class ClassLoader(object):
    @staticmethod
    def get_class(full_test_case_and_test_class_path):
        test_case_and_test_class_parts = full_test_case_and_test_class_path.split('.')
        test_case_path = ".".join(test_case_and_test_class_parts[:-1])
        m = __import__(test_case_path)
        for comp in test_case_and_test_class_parts[1:]:
            m = getattr(m, comp)
        return m

    @staticmethod
    def get_class_instance(full_test_case_and_test_class_path):
        class_instance_name = ClassLoader.get_class(full_test_case_and_test_class_path)
        return class_instance_name()

    @staticmethod
    def get_class_instance_with_arguments(full_test_case_and_test_class_path, arguments):
        class_instance_name = ClassLoader.get_class(full_test_case_and_test_class_path)
        return class_instance_name(arguments)
