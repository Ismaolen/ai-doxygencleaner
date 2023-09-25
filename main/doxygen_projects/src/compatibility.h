/**
 * @brief The UIDevice class provides access to information about the device such as battery state and orientation.
 */
@interface UIDevice ()

/**
 * @brief Sets the orientation of the device.
 *
 * @param orientation The new orientation of the device.
 */
- (void) setOrientation:(UIInterfaceOrientation)orientation;

/**
 * @brief A Boolean value indicating whether battery monitoring is enabled (YES) or not (NO).
 *
 * @return None
 */
@property(getter=isBatteryMonitoringEnabled) BOOL batteryMonitoringEnabled;

/**
 * @brief The current battery state of the device.
 *
 * @return None
 */
@property(readonly) UIDeviceBatteryState batteryState;

/**
 * @brief The current battery level of the device, ranging from 0.0 (empty) to 1.0 (full).
 *
 * @return None
 */
@property(readonly) float batteryLevel;

@end