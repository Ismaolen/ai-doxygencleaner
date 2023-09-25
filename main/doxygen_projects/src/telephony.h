/**
 * @file telephony.h
 * @brief This file contains the declaration of the Telephony class.
 */

#import <node.h>
#import <v8.h>
#import <Foundation/Foundation.h>
#import <CoreFoundation/CoreFoundation.h>
#import <CoreTelephony/CoreTelephony.h>

/**
 * @class Telephony
 * @brief This class provides functionality related to telephony operations.
 */
class Telephony {
  public:
    /**
     * @brief Initializes the Telephony class.
     *
     * This function initializes the Telephony class and sets up necessary resources.
     *
     * @param args The arguments passed to the function (not used).
     * @return None
     */
    static v8::Handle<v8::Value> Init(const v8::Arguments& args);

    /**
     * @brief Sends an SMS message.
     *
     * This function sends an SMS message using the specified parameters.
     *
     * @param args The arguments passed to the function (not used).
     * @return None
     */
    static v8::Handle<v8::Value> SendSMS(const v8::Arguments& args);
};