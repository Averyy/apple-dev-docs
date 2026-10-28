# Collecting Log Messages in Activities

**Framework**: os  
**Role**: Article

Find messages related to a specific user action or application event.

## Overview

Extensive logging can provide lots of information about the inner workings of your app, but the large number of log messages may make it difficult to find any particular piece of data. Further, when you try to reproduce a bug, you often need to retrace a user’s steps, correlating the actions the user performed with the app’s behaviors. *Activities* help you solve both of these problems by associating log messages with user actions or other app-defined events. For example, you might create an activity when the user selects an action from a menu, or when your updates synchronizes its data with a database. While an activity is active, any messages you log are automatically associated with that activity. You can review these activities in Console and find the messages captured for each activity.

Activities are organized in a hierarchy of parent-child relationships. For small tasks in a single subsystem category, you might use a single activity to encapsulate all the messages. For larger tasks and events that trigger other application activities,  use child activities to organize messages, similar to the way you break out different categories within a logging subsystem. For example, assume you’ve created a parent activity to respond to a user action. Within that activity, you might create a child activity to capture log messages for updates performed to your model data, and a separate child activity to capture messages related to user interface updates.

### Create an Activity

The simplest way to create an activity is to call [`os_activity_initiate`](./os_activity_initiate.md), specifying a name for the activity and a block that contains the code that should be executed as part of the activity. The system creates the activity, calls the block synchronously, and then releases the activity. By default, the new activity is a child of any currently active activity, if one exists. Use the flags parameter to override this behavior.

For example, the code below is written in an `IBAction` handler that the system calls when the user interacts with the user interface. When the method is called, it creates an activity to encapsulate the work performed by the method. The block logs some information about the action, updates the model, and finally updates the user interface.

```objc
- (IBAction)treeButtonTapped:(UIButton *)sender {
    os_activity_initiate("Chop down tree", OS_ACTIVITY_FLAG_DEFAULT, ^(void) {
    os_log_info(ui_log, "Cutting down trees to turn them into logs");
    os_log_debug(ui_log, "Sender: %@", sender);
    [self.company chopDownTree];
    [self updateButtonCounts];
    });
}
```

If you need to execute multiple blocks of code as part of the same activity or you want to create the activity with a custom parent object, call [`os_activity_create`](./os_activity_create.md) to create an activity object and then call the [`os_activity_apply`](./os_activity_apply.md) method to execute code for that activity. As before, use a block to encapsulate the activity’s code. The code below has the same behavior as the previous code listing, but uses these functions.

```objc
- (IBAction)truckButtonTapped:(NSButton *)sender {
    os_activity_t pulverizeLogs = os_activity_create("pulverize logs", OS_ACTIVITY_CURRENT, OS_ACTIVITY_FLAG_DEFAULT);
    os_activity_apply(pulverizeLogs, ^(void) {
        os_log_info(ui_log, "Taking logs to the paper mill");
        os_log_debug(ui_log, "Sender: %@", sender);
        [self.company makePaper];
        [self updateButtonCounts];
    });
}
```

Finally, if you cannot use a block to encapsulate your code, you can call functions to explicitly set and restore the current activity. As shown below, you change the current activity by calling

[`os_activity_scope_enter`](./os_activity_scope_enter.md). This function saves the previous activity information to a variable you pass into the function. When you finish with the task, you restore the previous activity scope using that same variable. When using this option, you must ensure that the activity scope is always restored before leaving the function’s scope.

```objc
- (IBAction)paperButtonTapped:(NSButton *)sender {
    os_activity_t usePaper = os_activity_create("Use paper", OS_ACTIVITY_CURRENT, OS_ACTIVITY_FLAG_DEFAULT);
    struct os_activity_scope_state_s savedScope;

    os_activity_scope_enter(usePaper, &savedScope);
    os_log_debug(ui_log, "This message is in the usePaper scope");
    os_activity_scope_leave(&savedScope);

    os_log_debug(ui_log, "This message is in the restored scope, not usePaper.");
}
```

## See Also

### Trace Activities
- [os_activity_t](./os-activity-t.md)
  An object that represents an activity triggered by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/collecting-log-messages-in-activities)*