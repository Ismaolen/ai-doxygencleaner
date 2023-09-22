/**
 * @file graphicServices.h
 * @brief This file contains the declaration of the GraphicServices class.
 */

#import <v8.h>
#import <node.h>
#import <GraphicsServices/GraphicsServices.h>

/**
 * @class GraphicServices
 * @brief This class provides access to private, undocumented APIs in the GraphicsServices framework.
 */
class GraphicServices {
  public:
    /**
     * @brief Initializes the GraphicServices class and adds it to the target object.
     * 
     * This function should be called in the module initialization function to expose the GraphicServices class to JavaScript.
     *
     * @param target The target object where the GraphicServices class will be added.
     */
    static void Init(v8::Handle<v8::Object> target);

    /**
     * @brief Locks the screen of the device.
     *
     * This function locks the screen of the device by calling GSEventLockDevice().
     *
     * @param args The arguments passed from JavaScript. Not used in this function.
     *
     * @return None
     */
    static v8::Handle<v8::Value> LockScreen(const v8::Arguments& args);

    /**
     * @brief Quits the top application on the device.
     *
     * This function quits the top application on the device by calling GSEventQuitTopApplication().
     *
     * @param args The arguments passed from JavaScript. Not used in this function.
     *
     * @return None
     */
    static v8::Handle<v8::Value> QuitTopApplication(const v8::Arguments& args);
};