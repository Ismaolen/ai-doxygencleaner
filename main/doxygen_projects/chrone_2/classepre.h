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
     * @brief Constructs a new Serial object.
     */
    Serial();

    /**
     * @brief Destroys the Serial object.
     */
    ~Serial();

    /**
     * @brief Reads a byte from the specified address in memory.
     *
     * @param address The address to read from.
     * @return The byte value read from the memory address.
     */
    byte ReadByte(const ushort& address);

    /**
     * @brief Writes a byte to the specified address in memory.
     *
     * @param address The address to write to.
     * @param val The byte value to write to the memory address.
     * @return True if the write operation was successful, false otherwise.
     */
    bool WriteByte(const ushort& address, const byte val);

private:
    byte m_Data;
};