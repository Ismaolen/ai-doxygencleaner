/**
 * @class Record
 * @brief This class represents a record in an address book.
 *
 * The Record class is a wrapper for the ABRecordID type in the AddressBook framework.
 * It provides a convenient way to access and manipulate records in an address book.
 */
class Record : public node::ObjectWrap {
  public:
    /**
     * @brief The unique identifier for the record.
     *
     * The recordId member variable stores the ABRecordID value that uniquely identifies
     * the record in the address book.
     */
    ABRecordID recordId;
}; // class Record