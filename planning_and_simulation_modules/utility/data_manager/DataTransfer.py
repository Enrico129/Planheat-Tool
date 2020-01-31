
class DataTransfer:
    study_id = 0

    def __init__(self):
        self.geo_graph = None
        self.buildings = None
        self.network = None
        self.tree_group = None
        self.tree_group_name = None
        self.baseline_scenario = None

        self.automatic_upload_network = False

        self.nb_selected_buildings_int_label = None
        self.total_pipe_length_int_label = None
        self.total_leastcost_length_int_label = None

        self.nb_used_sources_int_label = None
        self.total_covered_consumption_int_label = None

        self.dock_type = None
        self.step1_mode = False

        self.pipes_list = None

        self.save_network_on_exit = True

    def get_results(self):
        results = {}
        if self.nb_selected_buildings_int_label is not None:
            try:
                results["nb_selected_buildings_int_label"] = int(self.nb_selected_buildings_int_label.text())
            except ValueError:
                pass
        if self.total_pipe_length_int_label is not None:
            try:
                results["total_pipe_length_int_label"] = int(self.total_pipe_length_int_label.text()[0:-7])
            except ValueError:
                pass
        if self.total_leastcost_length_int_label is not None:
            try:
                results["total_leastcost_length_int_label"] = int(self.total_leastcost_length_int_label.text()[0:-7])
            except ValueError:
                pass
        if self.nb_used_sources_int_label is not None:
            try:
                results["nb_used_sources_int_label"] = int(self.nb_used_sources_int_label.text())
            except ValueError:
                pass
        if self.total_covered_consumption_int_label is not None:
            try:
                results["total_covered_consumption_int_label"] = int(self.total_covered_consumption_int_label.text()[0:-3])
            except ValueError:
                pass
        return results


    def get_building_layer_file_path(self):
        if self.buildings is not None:
            return self.buildings.dataProvider().dataSourceUri().split("|")[0]
        else:
            return None

    def print_state(self):
        if self.buildings is None:
            print("DataTransfer.py, print_state(). Buildings layer is None")
        else:
            print("DataTransfer.py, print_state(). Buildings layer:",  self.buildings.name(), "path:",
                  self.get_building_layer_file_path())
        if self.geo_graph is None:
            print("DataTransfer.py, print_state(). Graph is None")
        else:
            print("DataTransfer.py, print_state(). Graph is not empty:")
        if self.network is not None:
            print("DataTransfer.py, print_state(). Network is not None:", self.network.name)
        else:
            print("DataTransfer.py, print_state(). network is None:")
        if self.tree_group is not None:
            print("DataTransfer.py, print_state(). tree_group is not None:", self.tree_group)
        else:
            print("DataTransfer.py, print_state(). tree_group is None:")
        if self.tree_group is not None:
            print("DataTransfer.py, print_state(). tree_group_name is not None:", self.tree_group_name)
        else:
            print("DataTransfer.py, print_state(). tree_group_name is None:")
        if self.baseline_scenario is not None:
            print("DataTransfer.py, print_state(). baseline_scenario is not None:", self.baseline_scenario.name())
        else:
            print("DataTransfer.py, print_state(). baseline_scenario is None:")
        print("DataTransfer.py, print_state(). automatic_upload_network:", self.automatic_upload_network)
        print("DataTransfer.py, print_state(). automatic_upload_network:", self.dock_type)
        print("DataTransfer.py, print_state(). step1_mode:", self.step1_mode)
        print("DataTransfer.py, print_state(). pipes_list:", self.pipes_list)

    def print_graph(self):
        print("DataTransfer.py, print_graph(). self.geo_graph:")
        if self.geo_graph is not None:
            for node in self.geo_graph.nodes(data=True):
                print(node)
            for edge in self.geo_graph.edges(data=True):
                print(edge)
        else:
            print("None")

    def ready_check(self):
        return self.geo_graph is not None and self.buildings is not None
