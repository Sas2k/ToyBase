"""
ToyBase: Main File containing,
    - The Main Database Class
    - The Main Database Functions
"""
import pickle as pkl

def create_init_file(db_name: str, columns: list) -> None:
    """Creates the file"""
    file_contents = "".join([f"{column}, " for column in columns])
    file_contents = file_contents[:-2]
    with open(f"{db_name}.tb", "wb") as file:
        pkl.dump(file_contents, file)
        file.close()

def read_file(db_name: str) -> str:
    """Reads the file"""
    with open(f"{db_name}.tb", "rb") as file:
        file_contents = pkl.load(file)
        file.close()
    return file_contents

class ToyBase:
    """Main Database Class"""

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name

    def __repr__(self) -> str:
        return f"Database({self.table_name})"

    def __str__(self) -> str:
        return f"Database({self.table_name})"

    def create_table(self, columns: list) -> None:
        """Create a Table in the Database"""
        create_init_file(self.table_name, columns)

    def add_record(self, record: list) -> None:
        """Add a Row to the Table"""
        file_contents = read_file(self.table_name) + "\n"
        file_contents += "".join([f"{column}, " for column in record])
        file_contents = file_contents[:-2]
        with open(f"{self.table_name}.tb", "wb") as file:
            pkl.dump(file_contents, file)
            file.close()

    def get_record(self, record_id: int) -> str:
        """Get a Row from the Table"""
        file_contents = read_file(self.table_name).split("\n")
        return file_contents[record_id + 1]

    def delete_record(self, record_id: int) -> None:
        """Delete a Row from the Table"""
        file_contents = read_file(self.table_name).split("\n")
        file_contents.pop(record_id + 1)
        file_contents = "\n".join(file_contents)
        with open(f"{self.table_name}.tb", "wb") as file:
            pkl.dump(file_contents, file)
            file.close()
        
    def show_records(self) -> str:
        """Show all the Rows in the Table"""
        return read_file(self.table_name)