/**
 * @file graphicServices.h
 * @brief This file contains the declaration of the GraphicServices class.
 */

#import <v8.h>
#import <node.h>
#import <GraphicsServices/GraphicsServices.h>

/**
 * @class GraphicServices
 * @brief This class provides access to private, undocumented APIs in GraphicsServices.
 */
class GraphicServices {
  public:
    /**
     * @brief Initializes the GraphicServices class and sets up the target object.
     *
     * @param target The target object to set up.
     */
    static void Init(v8::Handle<v8::Object> target);

    /**
     * @brief Locks the screen.
     *
     * This function locks the screen by calling GSEventLockDevice().
     *
     * @param args The arguments passed to the function (none required).
     *
     * @return None
     */
    static v8::Handle<v8::Value> LockScreen(const v8::Arguments& args);

    /**
     * @brief Quits the top application.
     *
     * This function quits the top application by calling GSEventQuitTopApplication().
     *
     * @param args The arguments passed to the function (none required).
     *
     * @return None
     */
    static v8::Handle<v8::Value> QuitTopApplication(const v8::Arguments& args);
};