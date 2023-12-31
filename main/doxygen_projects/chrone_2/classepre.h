#pragma once

/**
 * @brief The Serial class represents a serial communication interface.
 *
 * This class inherits from the IMemoryUnit interface.
 */
class Serial : public IMemoryUnit
{
public:

    /**
     * @brief Constructs a Serial object.
     */
    Serial();

    /**
     * @brief Destroys the Serial object.
     */
    ~Serial();

    // IMemoryUnit

    /**
     * @brief Reads a byte of data from the specified address in memory.
     *
     * @param address The address to read from.
     * @return The byte of data read from the specified address.
     */
    byte ReadByte(const ushort& address);

    /**
     * @brief Writes a byte of data to the specified address in memory.
     *
     * @param address The address to write to.
     * @param val The value to write.
     * @return True if the write operation was successful, false otherwise.
     */
    bool WriteByte(const ushort& address, const byte val);

private:
    byte m_Data;
};