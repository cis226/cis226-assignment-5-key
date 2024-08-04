"""Program code"""

# Internal imports.
from beverage import BeverageRepository
from errors import AlreadyImportedError
from user_interface import UserInterface
from utils import CSVProcessor

# Set a constant for the path to the CSV file
PATH_TO_CSV = "./datafiles/beverage_list.csv"


def main(*args):
    """Method to run program"""

    # Create an instance of User Interface class
    ui = UserInterface()

    # Create an instance of the BeverageRepository class.
    beverage_repository = BeverageRepository()

    # Create an instance of the CSVProcessor class.
    csv_processor = CSVProcessor()

    # Display the Welcome Message to the user.
    ui.display_welcome_greeting()

    # Display the Menu and get the response. Store the response in the choice
    # integer. This is the 'primer' run of displaying and getting.
    choice = ui.display_menu_and_get_response()

    # While the choice is not exit program
    while choice != 7:
        if choice != 1 and not beverage_repository.database_exists:
            # Ensure that the database exists and has been loaded.
            ui.display_no_database_error()
        elif choice == 1:
            # Load the CSV File
            try:
                csv_processor.import_csv(beverage_repository, PATH_TO_CSV)
                ui.display_import_success()

            except AlreadyImportedError:
                ui.display_already_imported_error()
            except FileNotFoundError:
                ui.display_file_not_found_error()
            except EOFError:
                ui.display_empty_file_error()

        elif choice == 2:
            # Print Entire List Of Items
            all_item_string = str(beverage_repository)
            if all_item_string:
                ui.display_all_items(all_item_string)
            else:
                ui.display_all_items_error()

        elif choice == 3:
            # Search for an Item
            search_query = ui.get_search_query()
            item_info = beverage_repository.find_by_id(search_query)
            if item_info:
                ui.display_item_found(item_info)
            else:
                ui.display_item_found_error()

        elif choice == 4:
            # Collect information for a new item and add it to the repository
            new_item_info = ui.get_new_item_information()
            if beverage_repository.find_by_id(new_item_info[0]) is None:
                beverage_repository.add(
                    new_item_info[0],
                    new_item_info[1],
                    new_item_info[2],
                    float(new_item_info[3]),
                    new_item_info[4] == "True",
                )
                ui.display_add_beverage_success()
            else:
                ui.display_beverage_already_exists_error()

        elif choice == 5:
            # Update an existing item in the database
            # Search for an item to update
            update_search_query = ui.get_update_search_query()
            # Check to make sure item exists in the database
            success = beverage_repository.item_exists(update_search_query)
            # If it does exist
            if success:
                # Get the properties to update
                updated_properties = ui.get_updated_item_information()
                updated_price = updated_properties[2]
                if updated_price:
                    updated_price = float(updated_price)
                updated_active = updated_properties[3]
                if updated_active is not None:
                    updated_active = updated_active == "True"

                # Update the item and get back a bool as the result
                update_success = beverage_repository.update(
                    update_search_query,
                    updated_properties[0],
                    updated_properties[1],
                    updated_price,
                    updated_active,
                )

                # If successful, display success, else error
                if update_success:
                    ui.display_beverage_update_success()
                else:
                    ui.display_beverage_update_error()
            else:
                ui.display_item_found_error()

        elif choice == 6:
            # Delete an existing item from the database
            # Search for item to delete
            delete_search_query = ui.get_delete_search_query()
            # Check to make sure item exists in the database
            beverage = beverage_repository.find_by_id(delete_search_query)
            # If it does exist
            if beverage:
                # Check to make sure user wants to delete.
                confirmed = ui.get_delete_confirmation(beverage)
                # if confirmed, attempt delete.
                if confirmed:
                    # Attempt to delete the item
                    success = beverage_repository.delete(delete_search_query)
                    if success:
                        ui.display_beverage_delete_success()
                    else:
                        ui.display_beverage_delete_error()
                else:
                    ui.display_beverage_delete_abort()
            else:
                ui.display_item_found_error()

        # Get the new choice of what to do from the user.
        choice = ui.display_menu_and_get_response()
