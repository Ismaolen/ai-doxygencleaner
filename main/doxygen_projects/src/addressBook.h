/**
 * @class AddressBook
 * @brief This class provides functions to interact with the Address Book.
 */
class AddressBook {
  public:
    /**
     * @brief Initializes the Address Book module.
     *
     * This function should be called to initialize the Address Book module before using any other functions.
     *
     * @param target The target object to attach the Address Book module to.
     */
    static void Init(v8::Handle<v8::Object> target);

    /**
     * @brief Retrieves all contacts from the Address Book.
     *
     * This function retrieves all contacts from the Address Book and returns them as an array of objects.
     *
     * @param args The arguments passed to the function. None required.
     *
     * @return An array of contact objects retrieved from the Address Book.
     */
    static v8::Handle<v8::Value> GetContacts(const v8::Arguments& args);

    /**
     * @brief Retrieves all groups from the Address Book.
     *
     * This function retrieves all groups from the Address Book and returns them as an array of objects.
     *
     * @param args The arguments passed to the function. None required.
     *
     * @return An array of group objects retrieved from the Address Book.
     */
    static v8::Handle<v8::Value> GetGroups(const v8::Arguments& args);

    /**
      *@brief Saves changes made to a contact in the Address Book
      *
      *@param args The arguments passed to the function. It should contain a contact object with changes made to it, and an optional callback function that will be called after saving is complete. 
      *
      *@return None
      */
    static v8::Handle<v8::Value> Save(const v8::Arguments& args);
};

/**
  *@struct async_request
  *@brief Represents an asynchronous request for retrieving contacts from the Address Book.
  */
struct async_request {
  v8::Persistent<v8::Function> cb; /**< The callback function to be called after the request is complete. */
  bool hasCb; /**< Indicates whether a callback function is provided or not. */
  CFIndex resultsCount; /**< The number of results returned by the request. */
  Record **results; /**< An array of pointers to "Record" instances representing the results of the request. */
};