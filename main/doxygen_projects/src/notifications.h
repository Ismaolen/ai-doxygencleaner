#import <node.h>
#import <v8.h>
#import <unistd.h>
#import <Foundation/Foundation.h>
#import <CoreFoundation/CoreFoundation.h>
#import <CoreFoundation/CFUserNotification.h>

/**
 * @brief Structure to hold notification request details.
 */
struct notification_request {
  CFOptionFlags options; /**< Options for the notification. */
  CFUserNotificationRef notif; /**< Reference to the user notification. */
  SInt32 error; /**< Error code if any occurred during the notification creation. */
  v8::Persistent<v8::Function> cb; /**< Callback function for the notification. */
  bool hasCb; /**< Flag indicating whether a callback function is provided or not. */
};

/**
 * @brief Class that provides functions to create notifications.
 *
 * This class provides static functions to initialize and create notifications.
 */
class Notifications {
public:
    /**
     * @brief Initializes the Notifications class and attaches it to the target object.
     *
     * This function should be called in the module initialization function to attach
     * the Notifications class to the target object in Node.js.
     *
     * @param target The target object where the Notifications class will be attached.
     */
    static void Init(v8::Handle<v8::Object> target);

    /**
     * @brief Creates a new user notification with the provided arguments.
     *
     * This function creates a new user notification based on the arguments passed from Node.js.
     *
     * @param args The arguments passed from Node.js containing information about the notification.
     *
     * @return None
     */
    static v8::Handle<v8::Value> createNotification(const v8::Arguments& args);
};