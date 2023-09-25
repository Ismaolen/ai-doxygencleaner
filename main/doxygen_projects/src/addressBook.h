/**
 * @class AddressBook
 * @brief This class provides functions to interact with the Address Book on macOS.
 */

/**
 * @fn void AddressBook::Init(v8::Handle<v8::Object> target)
 * @brief Initializes the AddressBook class and adds it to the target object.
 * @param target The target object to add the AddressBook class to.
 */

/**
 * @fn v8::Handle<v8::Value> AddressBook::GetContacts(const v8::Arguments& args)
 * @brief Retrieves all contacts from the Address Book.
 * @param args The arguments passed to the function (none required).
 * @return An array of contact objects.
 */

/**
 * @fn v8::Handle<v8::Value> AddressBook::GetGroups(const v8::Arguments& args)
 * @brief Retrieves all groups from the Address Book.
 * @param args The arguments passed to the function (none required).
 * @return An array of group objects.
 */

/**
 * @fn v8::Handle<v8::Value> AddressBook::Save(const v8::Arguments& args)
 * @brief Saves changes made to the Address Book.
 * @param args The arguments passed to the function (none required).
 */