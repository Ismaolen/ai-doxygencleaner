/**
 * @brief The UIDevice class provides a way to access and manipulate information about the device.
 *
 * This class is a singleton, meaning that only one instance of it can exist at any given time.
 */
@interface UIDevice ()

/**
 * @brief Sets the orientation of the device.
 *
 * @param orientation The new orientation of the device.
 */
- (void) setOrientation:(UIInterfaceOrientation)orientation;

/**
 * @brief A Boolean value indicating whether battery monitoring is enabled for the device.
 *
 * If this property is set to YES, the device will monitor changes in battery state and update
 * the batteryState and batteryLevel properties accordingly. If set to NO, battery monitoring
 * will be disabled.
 */
@property(getter=isBatteryMonitoringEnabled) BOOL batteryMonitoringEnabled;

/**
 * @brief The current state of the device's battery.
 *
 * This property represents the current state of the device's battery. It can have one of four values:
 * - UIDeviceBatteryStateUnknown: The state of the battery is unknown.
 * - UIDeviceBatteryStateUnplugged: The device is on battery power and discharging.
 * - UIDeviceBatteryStateCharging: The device is plugged in and charging, but not yet at 100% capacity.
 * - UIDeviceBatteryStateFull: The device is plugged in and fully charged (at 100% capacity).
 */
@property(readonly) UIDeviceBatteryState          batteryState;

/**
 * @brief The current level of charge on the device's battery.
 *
 * This property represents the current level of charge on the device's battery as a floating-point value
 * between 0.0 (empty) and 1.0 (full). If no battery monitoring is enabled or if there are errors in obtaining
 * this information, this property will return -1.0.
 */
@property(readonly) float                         batteryLevel;

@end