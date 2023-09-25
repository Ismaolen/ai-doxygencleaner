/**
 * @class Contact
 * @brief Represents a contact in an address book.
 *
 * This class inherits from the base class Record and adds additional fields to represent a person's contact information.
 */
class Contact : public Record {
  public:
    /**
     * @brief The first name of the contact.
     */
    const char *firstName;
    
    /**
     * @brief The middle name of the contact.
     */
    const char *middleName;
    
    /**
     * @brief The last name of the contact.
     */
    const char *lastName;
    
    /**
     * @brief The organization of the contact.
     */
    const char *organization;
    
    /**
     * @brief The job title of the contact.
     */
    const char *jobTitle;
    
    /**
     * @brief The department of the contact.
     */
    const char *department;
    
    /**
     * @brief The number of phone numbers associated with the contact.
     */
    int numNumbers;
    
    /**
     * @brief An array containing names for each phone number associated with the contact.
     */
    const char **numbersNames;
    
    /**
     * @brief An array containing values for each phone number associated with the contact.
     */
    const char **numbersValues;
}; // class Contact