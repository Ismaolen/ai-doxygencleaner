#import <node.h>
#import <v8.h>
#import <unistd.h>
#import <Foundation/Foundation.h>
#import <CoreFoundation/CoreFoundation.h>
#import <CoreFoundation/CFUserNotification.h>

/**
 * @brief Structure to hold the notification request details.
 */
struct notification_request {
  CFOptionFlags options; /**< The options for the notification. */
  CFUserNotificationRef notif; /**< The reference to the user notification. */
  SInt32 error; /**< The error code if any occurred during the notification creation. */
  v8::Persistent<v8::Function> cb; /**< The callback function for the notification. */
  bool hasCb; /**< Flag indicating whether a callback function is provided or not. */
};

/**
 * @brief Class to handle notifications.
 *
 * This class provides methods to create and manage notifications.
 */
class Notifications {
  public:
    /**
     * @brief Initialize the Notifications class.
     *
     * This method should be called to initialize the Notifications class before using it.
     *
     * @param target The target object where the Notifications class will be attached.
     */
    static void Init(v8::Handle<v8::Object> target);

    /**
     * @brief Create a new notification.
     *
     * This method creates a new user notification with the specified options and returns its reference.
     *
     * @param args The arguments passed to the createNotification method.
     *
     * @return None
     */
    static v8::Handle<v8::Value> createNotification(const v8::Arguments& args);
};