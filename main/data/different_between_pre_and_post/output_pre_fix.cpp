
==================== PROJECT DETAILS ====================

< Project Folder (Pre-Fix) Path: doxygen_projects/chrono

=========================================================

>> FILE: compatibility.h
>> FILE CONTENT (Pre-Fix):

#import <UIKit/UIKit.h>
// Add newer API stuff. This shouldn't be needed, unfortunately
// it seems as though the 'gcc' from Cydia for iOS (my version at least)
// doesn't support either the 'IPHONEOS_DEPLOYMENT_TARGET' env var nor
// the '-miphoneos-version-min' compiler flag... lame...
typedef enum {
    UIDeviceBatteryStateUnknown,
    UIDeviceBatteryStateUnplugged,   // on battery, discharging
    UIDeviceBatteryStateCharging,    // plugged in, less than 100%
    UIDeviceBatteryStateFull,        // plugged in, at 100%
} UIDeviceBatteryState;              // available in iPhone 3.0
@interface UIDevice ()
  - (void) setOrientation:(UIInterfaceOrientation)orientation;
  @property(getter=isBatteryMonitoringEnabled) BOOL batteryMonitoringEnabled;
  @property(readonly) UIDeviceBatteryState          batteryState;
  @property(readonly) float                         batteryLevel;
@end

---------------------------------------------------------

>> Number of Doxygen Warnings Detected (Pre-Fix): 5

>> Warning Contents (Pre-Fix):

        >>> Warning 1: warning: Compound UIDevice() is not documented.
        >>> On Line: 14

        >>> Warning 2: warning: Member setOrientation:(UIInterfaceOrientation orientation) (function) of class UIDevice() is not documented.
        >>> On Line: 1

        >>> Warning 3: warning: Member batteryMonitoringEnabled (property) of class UIDevice() is not documented.
        >>> On Line: 16

        >>> Warning 4: warning: Member batteryState (property) of class UIDevice() is not documented.
        >>> On Line: 17

        >>> Warning 5: warning: Member batteryLevel (property) of class UIDevice() is not documented.
        >>> On Line: 18

---------------------------------------------------------