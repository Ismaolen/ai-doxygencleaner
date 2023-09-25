/**
 * @class Record
 * @brief Represents a record in an address book.
 *
 * This class is used to store information about a record in an address book.
 */
class Record : public node::ObjectWrap {
  public:
    ABRecordID recordId; /**< The unique identifier of the record. */
}; // class Record