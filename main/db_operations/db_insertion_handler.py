import os
import time

from error_handler.error_handler import ErrorHandler
from transport_data.transport_data import save_data_to_json
from dotenv import load_dotenv
import MySQLdb as mdb

FIXED_STATUS_DEFAULT = 1


class DBInsertionHandler:
    """
    Handles database insert operations for doxygen warnings.

    This class manages connections to a MySQL database and provides methods for
    inserting information related to doxygen warnings, such as details about the
    pipeline, project, and warnings themselves.
    ...

    Attributes
    ----------
    __db_name : str
        Name of the database.
    __db_host : str
        Host of the database.
    __db_user : str
        Username to connect to the database.
    __db_pass : str
        Password to connect to the database.
    last_header_file_id : int
        The ID of the last inserted header file.
    last_project_id : int
        The ID of the last inserted project.
    pipeline_link : str
        The link to the GitLab pipeline.
    branch_name : str
        The branch name in the repository.
    pipeline_id : int
        The ID of the pipeline.
    cursor : Cursor
        A MySQL database cursor to execute SQL commands.
    db : Connection
        A MySQL database connection.

    Methods
    -------

    connect_to_database():
        Connects to the MySQL database using environment variables.

    create_cursor():
        Creates a new cursor to execute database commands.

    set_pipeline_data():
        Sets pipeline data by getting information from environment variables. If no pipeline ID is
        provided, generates a pseudo-random one.

    update_last_project_id():
        Updates the last_project_id member variable with the most recent project ID.

    update_last_header_file_id():
        Updates the last_header_file_id member variable with the most recent header file ID.

    execute_sql(sql: str, values: tuple, optional):
        Executes a SQL command.

    insert_into_pipeline_table():
        Inserts pipeline details into the pipeline table.

    insert_into_project_table(project_folder_path: str):
        Inserts project details into the project table and updates the last project ID.

    insert_into_header_file_table(file_name: str, file_content: str, number_of_warnings: int):
        Inserts header file details into the header file table and updates the last header file ID.

    insert_into_warning_table_pre_fix(warning_content: str, line_number_pre_fix: int, fixed_status: int =
    FIXED_STATUS_DEFAULT):
        Inserts warning details into the warning table.

    insert_warnings_details(project_folder_path: str, file_name_list: list, file_content_list: list,
    number_of_warnings_list: list, warning_content_llist: list, line_number_pre_fix_llist: list):
        Wrapper function that inserts pipeline, project, header file, and warning details into their respective tables.
        Once the data is inserted, it commits the changes and closes the database connection.

    update_post_fix_warning_details(self, pipeline_id, file_name_list, file_content_list, line_number_llist,
    warnings_content_llist):
    Update the database with the details of post-fix warnings.
    """

    def __init__(self):
        """
        Initializes a new DBInsertionHandler instance.

        During initialization, environment variables are loaded, a database
        connection is established, and data related to the pipeline is set.
        """
        # Load database environment variables
        load_dotenv("config/db_local_variables.env")
        self.__db_name = os.getenv('DBNAME')
        self.__db_host = os.getenv('DBHOST')
        self.__db_user = os.getenv('DBUSER')
        self.__db_pass = os.getenv('DBPASS')
        # Initialize member variables to hold various IDs
        self.last_header_file_id = None
        self.last_project_id = None
        self.pipeline_link = None
        self.branch_name = None
        self.pipeline_id = None
        self.cursor = None
        self.db = None
        self.error_handler = ErrorHandler()
        # ErrorHandler.__init__(self)
        # Establish connection to database and setup pipeline data
        self.connect_to_database()
        self.create_cursor()

    def connect_to_database(self):
        """
        Establishes a connection to the MySQL database using the details obtained from the environment variables.

        Raises
        ------
        Exception
            If there is an error while establishing the database connection.
        """

        self.db = mdb.connect(self.__db_host, self.__db_user, self.__db_pass, self.__db_name)

    def create_cursor(self):
        """
        Creates a new cursor to execute database commands.

        Raises
        ------
        Exception
            If there is an error while creating a cursor.
        """
        self.cursor = self.db.cursor()

    def set_pipeline_data(self):
        """
        Sets pipeline data by getting information from environment variables. If no pipeline ID is provided,
        generates a pseudo-random one.
        """
        """
        Sets pipeline data by getting information from environment variables.
        If no pipeline ID is provided, generates a pseudo-random one.
        Raises
        ----------
        Exception
            If necessary environment variables are not set.
        """
        self.pipeline_id = os.getenv('CI_PIPELINE_ID')
        self.branch_name = os.getenv('CI_COMMIT_BRANCH')
        self.pipeline_link = f"https://gitlab.rz.htw-berlin.de/" \
                             f"{os.getenv('CI_PROJECT_NAMESPACE')}/" \
                             f"{os.getenv('CI_PROJECT_NAME')}" \
                             f"/-/pipelines/{os.getenv('CI_PIPELINE_ID')}"
        if self.pipeline_id is None:
            # Generate a pseudo-random pipeline ID if none is provided
            self.pipeline_id = int(time.time() * 1000) % 1000000
        data = {"pipeline_id": self.pipeline_id}
        save_data_to_json("transport_data/pipeline_id.json", data)
        print(f'\033[1;91m>> Pipeline ID: \033[0m'
              f'\033[4;32m{self.pipeline_id}\033[0m\n')

    def update_last_project_id(self):
        """
        Updates the last_project_id member variable with the most recent project ID from the database.

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        sql = 'Select @LastProjektID;'
        self.error_handler.execute_sql(self.cursor, sql)
        self.last_project_id = self.cursor.fetchone()[0]
        print(f'\033[1;94m\t>>> Project ID: \033[0m'
              f'\033[4;32m{self.last_project_id}\033[0m\n')

    def update_last_header_file_id(self):
        """
        Updates the last_header_file_id member variable with the most recent header file ID from the database.

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        sql = 'SELECT @header_file_id_output;'
        self.error_handler.execute_sql(self.cursor, sql)
        self.last_header_file_id = self.cursor.fetchone()[0]
        print(f'\033[1;95m\t\t>>>> Header File ID: \033[0m'
              f'\033[4;32m{self.last_header_file_id}\033[0m')

    def insert_into_pipeline_table(self):
        """
        Inserts pipeline details into the pipeline table in the database.

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        sql = "CALL InsertIntoPipelineTable(%s, %s, %s);"
        params = (self.pipeline_id, self.branch_name, self.pipeline_link)
        self.error_handler.execute_sql(self.cursor, sql, params)

    def insert_into_project_table(self, project_folder_path):
        """
        Inserts project details into the project table and updates the last project ID.

        Parameters
        ----------
        project_folder_path : str
            The path to the project folder.

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        sql = "CALL InsertIntoProjectTable(%s, %s, @LastProjektID);"
        params = (self.pipeline_id, project_folder_path)
        self.error_handler.execute_sql(self.cursor, sql, params)
        self.update_last_project_id()

    def insert_into_header_file_table(self, file_name, file_content, number_of_warnings):
        """
        Inserts header file details into the header file table and updates the last header file ID.

        Parameters
        ----------
        file_name : str
            The name of the header file.
        file_content : str
            The content of the header file.
        number_of_warnings : int
            The number of warnings in the header file.

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        sql = "CALL InsertIntoHeaderFileTable(%s, %s, %s, %s, @header_file_id_output);"
        params = (self.last_project_id, file_name, file_content, number_of_warnings)
        self.error_handler.execute_sql(self.cursor, sql, params)
        self.update_last_header_file_id()

    def insert_into_warning_table_pre_fix(self, warning_content, line_number_pre_fix,
                                          fixed_status=FIXED_STATUS_DEFAULT):
        """
        Inserts the warning details into the warning table before the warnings are resolved by ChatGPT.

        Parameters
        ----------
        warning_content : str
            The content of the warning.
        line_number_pre_fix : int
            The line number of the warning before fixing by ChatGPT.
        fixed_status : int, optional
            The fixed status of the warning (default is FIXED_STATUS_DEFAULT).

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        sql = "CALL InsertIntoWarningTablePreFix(%s, %s, %s, %s, 'Pre-Fix');"
        params = (self.last_header_file_id, warning_content, line_number_pre_fix, fixed_status)
        self.error_handler.execute_sql(self.cursor, sql, params)

    def insert_warnings_details(self, project_folder_path, file_name_list, file_content_list,
                                number_of_warnings_list, warning_content_llist,
                                line_number_pre_fix_llist):
        """
        Wrapper function that inserts pipeline, project, header file, and warning details into their respective tables.
        Once the data is inserted, it commits the changes and closes the database connection.

        Parameters
        ----------
        project_folder_path : str
            The path to the project folder.
        file_name_list : list
            The list of file names.
        file_content_list : list
            The list of file contents.
        number_of_warnings_list : list
            The list of the number of warnings per file.
        warning_content_llist : list
            The list of warning contents.
        line_number_pre_fix_llist : list
            The list of line numbers of warnings before fixing.

        Raises
        ------
        Exception
            If there is an error while executing the SQL commands.
        """
        self.set_pipeline_data()
        self.insert_into_pipeline_table()
        self.insert_into_project_table(project_folder_path)
        for file_name, file_content, number_of_warnings, warning_content_list, \
                line_number_pre_fix_list in zip(file_name_list, file_content_list, number_of_warnings_list,
                                                warning_content_llist, line_number_pre_fix_llist):
            self.insert_into_header_file_table(file_name, file_content, number_of_warnings)
            for warning_content, line_number_pre_fix in zip(warning_content_list, line_number_pre_fix_list):
                self.insert_into_warning_table_pre_fix(warning_content, line_number_pre_fix, FIXED_STATUS_DEFAULT)
        # Commit all changes to the database
        self.db.commit()
        # Close the database connection
        self.db.close()

    def update_post_fix_warning_details(self, pipeline_id, file_name_list: list,
                                        file_content_list: list, line_number_llist: list, warnings_content_llist: list):
        """
        Update the database with the details of post-fix warnings.

        This method updates the header file content and warning fixed status in the database. It loops
        through the given list of file names, updates each file's content, and then checks if there
        are any warnings. If there are, it sets the fixed status to 0 and updates this in the database.

        Parameters
        ----------
        pipeline_id : str
            The ID of the current pipeline.
        file_name_list : list
            A list of the names of the files to update.
        file_content_list : list
            A list containing the content of the files.
        line_number_llist : list
            A list of lists, each sublist contains the line numbers where warnings occurred.
        warnings_content_llist : list
            A list of lists, each sublist contains the warning content from a file.

        Raises
        ------
        Exception
            If there is an error while executing the SQL commands.
        """
        print(f'\033[1;91m>> Pipeline ID: \033[0m'
              f'\033[4;32m{pipeline_id}\033[0m\n')

        # Loop through the list of file names and update each file's content in the database
        for pos, file_name in enumerate(file_name_list):
            sql1 = 'CALL UpdateHeaderFileContentPostFix(%s, %s, %s);'
            params = pipeline_id, file_name, file_content_list[pos]
            self.error_handler.execute_sql(self.cursor, sql1, params)

            # If there are no warnings for this file, skip to the next file
            if warnings_content_llist[pos] is None:
                continue

            # For each warning, update the fixed status in the database
            for index, warnings_content in enumerate(warnings_content_llist[pos]):
                sql2 = 'CALL UpdateFixedStatusPostFix(%s, %s, %s, %s, %s);'
                fixed_status = 0  # if warning found, it means the warning is not fixed
                params = (line_number_llist[pos][index], fixed_status, pipeline_id, file_name, warnings_content)
                self.error_handler.execute_sql(self.cursor, sql2, params)

        # Discard any remaining result sets
        while self.cursor.nextset():
            pass

        # Commit all changes to the database
        self.db.commit()

        # Close the database connection
        self.db.close()
