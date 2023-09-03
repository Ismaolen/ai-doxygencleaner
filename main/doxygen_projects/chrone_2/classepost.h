#pragma once

class Serial : public IMemoryUnit
{
public:
    /**
     * @brief Constructs a new Serial object.
     */
    Serial();

    ~Serial();

    // IMemoryUnit

    /**
     * @brief Reads a byte from the specified address in memory.
     *
     * @param address The address to read from.
     * @return The byte value read from memory.
     */
    byte ReadByte(const ushort& address);

    /**
     * @brief Writes a byte to the specified address in memory.
     *
     * @param address The address to write to.
     * @param val The byte value to write.
     * @return True if the write operation was successful, false otherwise.
     */
    bool WriteByte(const ushort& address, const byte val);

private:
    byte m_Data; ///< Member variable to hold data.
};

/**
 * @class Serial
 * 
 * @brief Represents a serial communication interface that implements the IMemoryUnit interface. 
 *
 * This class provides methods for reading and writing bytes from/to memory addresses. It also has a member variable m_Data to store data.