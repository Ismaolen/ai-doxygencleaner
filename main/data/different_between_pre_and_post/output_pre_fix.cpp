
==================== PROJECT DETAILS ====================

< Project Folder (Pre-Fix) Path: doxygen_projects/src

=========================================================

>> FILE: telephony.h
>> FILE CONTENT (Pre-Fix):

#import <node.h>
#import <v8.h>
#import <Foundation/Foundation.h>
#import <CoreFoundation/CoreFoundation.h>
#import <CoreTelephony/CoreTelephony.h>

class Telephony {
  public:
    static v8::Handle<v8::Value> Init(const v8::Arguments& args);
    static v8::Handle<v8::Value> SendSMS(const v8::Arguments& args);
};

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 3

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound Telephony is not documented.
	>>> On Line: 7

	>>> Warning 2: warning: Member Init(const v8::Arguments &args) (function) of class Telephony is not documented.
	>>> On Line: 9

	>>> Warning 3: warning: Member SendSMS(const v8::Arguments &args) (function) of class Telephony is not documented.
	>>> On Line: 10

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
=========================================================

>> FILE: addressBook.h
>> FILE CONTENT (Pre-Fix):

#import <node.h>
#import <v8.h>
#import <CoreFoundation/CoreFoundation.h>
#import <Foundation/Foundation.h>
#import <AddressBook/AddressBook.h>
#import "addressBook-Record.h"
#import "addressBook-Contact.h"

int GetContacts_DoRequest (eio_req *);
int GetContacts_AfterResponse (eio_req *);

struct async_request {
  v8::Persistent<v8::Function> cb;
  bool hasCb;
  CFIndex resultsCount;
  // 'results' is an array of pointers to "Record" instances
  Record **results;
};

class AddressBook {
  public:
    static void Init(v8::Handle<v8::Object> target);
    static v8::Handle<v8::Value> GetContacts(const v8::Arguments& args);
    static v8::Handle<v8::Value> GetGroups(const v8::Arguments& args);
    static v8::Handle<v8::Value> Save(const v8::Arguments& args);
};

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 10

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound AddressBook is not documented.
	>>> On Line: 20

	>>> Warning 2: warning: Compound async_request is not documented.
	>>> On Line: 12

	>>> Warning 3: warning: Member Init(v8::Handle< v8::Object > target) (function) of class AddressBook is not documented.
	>>> On Line: 22

	>>> Warning 4: warning: Member GetContacts(const v8::Arguments &args) (function) of class AddressBook is not documented.
	>>> On Line: 23

	>>> Warning 5: warning: Member GetGroups(const v8::Arguments &args) (function) of class AddressBook is not documented.
	>>> On Line: 24

	>>> Warning 6: warning: Member Save(const v8::Arguments &args) (function) of class AddressBook is not documented.
	>>> On Line: 25

	>>> Warning 7: warning: Member cb (variable) of struct async_request is not documented.
	>>> On Line: 13

	>>> Warning 8: warning: Member hasCb (variable) of struct async_request is not documented.
	>>> On Line: 14

	>>> Warning 9: warning: Member resultsCount (variable) of struct async_request is not documented.
	>>> On Line: 15

	>>> Warning 10: warning: Member results (variable) of struct async_request is not documented.
	>>> On Line: 17

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
=========================================================

>> FILE: graphicServices.h
>> FILE CONTENT (Pre-Fix):

#import <v8.h>
#import <node.h>
#import <GraphicsServices/GraphicsServices.h>

/* Private, undocumented APIs */
//void GSEventLockDevice();
//void GSEventQuitTopApplication();

class GraphicServices {
  public:
    static void Init(v8::Handle<v8::Object> target);
    static v8::Handle<v8::Value> LockScreen(const v8::Arguments& args);
    static v8::Handle<v8::Value> QuitTopApplication(const v8::Arguments& args);
};

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 4

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound GraphicServices is not documented.
	>>> On Line: 9

	>>> Warning 2: warning: Member Init(v8::Handle< v8::Object > target) (function) of class GraphicServices is not documented.
	>>> On Line: 11

	>>> Warning 3: warning: Member LockScreen(const v8::Arguments &args) (function) of class GraphicServices is not documented.
	>>> On Line: 12

	>>> Warning 4: warning: Member QuitTopApplication(const v8::Arguments &args) (function) of class GraphicServices is not documented.
	>>> On Line: 13

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
=========================================================

>> FILE: addressBook-Record.h
>> FILE CONTENT (Pre-Fix):

#import <node.h>
#import <AddressBook/AddressBook.h>

class Record : public node::ObjectWrap {
  public:
    ABRecordID recordId;
}; // class Record

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 2

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound Record is not documented.
	>>> On Line: 4

	>>> Warning 2: warning: Member recordId (variable) of class Record is not documented.
	>>> On Line: 6

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
=========================================================

>> FILE: addressBook-Contact.h
>> FILE CONTENT (Pre-Fix):

#import "addressBook-Record.h"

class Contact : public Record {
  public:
    // Person
    const char *firstName;
    const char *middleName;
    const char *lastName;
    // Organization
    const char *organization;
    const char *jobTitle;
    const char *department;
    // Phone Numbers
    int numNumbers;
    const char **numbersNames;
    const char **numbersValues;
}; // class Contact

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 10

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound Contact is not documented.
	>>> On Line: 3

	>>> Warning 2: warning: Member firstName (variable) of class Contact is not documented.
	>>> On Line: 6

	>>> Warning 3: warning: Member middleName (variable) of class Contact is not documented.
	>>> On Line: 7

	>>> Warning 4: warning: Member lastName (variable) of class Contact is not documented.
	>>> On Line: 8

	>>> Warning 5: warning: Member organization (variable) of class Contact is not documented.
	>>> On Line: 10

	>>> Warning 6: warning: Member jobTitle (variable) of class Contact is not documented.
	>>> On Line: 11

	>>> Warning 7: warning: Member department (variable) of class Contact is not documented.
	>>> On Line: 12

	>>> Warning 8: warning: Member numNumbers (variable) of class Contact is not documented.
	>>> On Line: 14

	>>> Warning 9: warning: Member numbersNames (variable) of class Contact is not documented.
	>>> On Line: 15

	>>> Warning 10: warning: Member numbersValues (variable) of class Contact is not documented.
	>>> On Line: 16

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
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

	>>> Warning 2: warning: Member setOrientation:(UIInterfaceOrientation orientation) (function) of category UIDevice() is not documented.
	>>> On Line: 1

	>>> Warning 3: warning: Member batteryMonitoringEnabled (property) of category UIDevice() is not documented.
	>>> On Line: 16

	>>> Warning 4: warning: Member batteryState (property) of category UIDevice() is not documented.
	>>> On Line: 17

	>>> Warning 5: warning: Member batteryLevel (property) of category UIDevice() is not documented.
	>>> On Line: 18

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
=========================================================

>> FILE: notifications.h
>> FILE CONTENT (Pre-Fix):

#import <node.h>
#import <v8.h>
#import <unistd.h>
#import <Foundation/Foundation.h>
#import <CoreFoundation/CoreFoundation.h>
#import <CoreFoundation/CFUserNotification.h>

int CreateNotification_WaitForResponse (eio_req *);
int CreateNotification_AfterResponse (eio_req *);

struct notification_request {
  CFOptionFlags options;
  CFUserNotificationRef notif;
  SInt32 error;
  v8::Persistent<v8::Function> cb;
  bool hasCb;
};

class Notifications {
  public:
    static void Init(v8::Handle<v8::Object> target);
    static v8::Handle<v8::Value> createNotification(const v8::Arguments& args);
};

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 9

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound Notifications is not documented.
	>>> On Line: 19

	>>> Warning 2: warning: Compound notification_request is not documented.
	>>> On Line: 11

	>>> Warning 3: warning: Member options (variable) of struct notification_request is not documented.
	>>> On Line: 12

	>>> Warning 4: warning: Member notif (variable) of struct notification_request is not documented.
	>>> On Line: 13

	>>> Warning 5: warning: Member error (variable) of struct notification_request is not documented.
	>>> On Line: 14

	>>> Warning 6: warning: Member cb (variable) of struct notification_request is not documented.
	>>> On Line: 15

	>>> Warning 7: warning: Member hasCb (variable) of struct notification_request is not documented.
	>>> On Line: 16

	>>> Warning 8: warning: Member Init(v8::Handle< v8::Object > target) (function) of class Notifications is not documented.
	>>> On Line: 21

	>>> Warning 9: warning: Member createNotification(const v8::Arguments &args) (function) of class Notifications is not documented.
	>>> On Line: 22

---------------------------------------------------------

2023-09-25 16:17:23 - File analysis completed.
=========================================================

