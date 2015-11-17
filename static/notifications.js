// Ask the browser for permission to show notifications
// Taken from https://developer.mozilla.org/en-US/docs/Web/API/Notification/Using_Web_Notifications
window.addEventListener('load', function(){
	Notification.requestPermission(function(status){
		// This allows to use Notification.permission with Chrome/Safari
		if (Notification.permission != status){
			Notification.permission = status;
		}
	});
});

// Create an instance of vanilla dragon
var dragon = new VanillaDragon({onopen: onOpen, onchannelmessage: onChannelMessage});

// This is the list of notifications
var notificationsList = document.getElementById("notifications-section");

// New channel message recieved
function onChannelMessage(channels, message){
	// Add the notification
	addNotification((message.data));
}

function onOpen(){
	// Once the connection is open, subscribe to notifications
	dragon.subscribe('notifications', 'notifications');
}

// Add new notifications
function addNotification(notification){
	// If we have permission to show browser notifications
	// we can show the notification
	if(window.Notification && Notification.permission === "granted"){
		new Notification(notification.message);
	}

	// Add the new notification
	var li = document.createElement("li");
	notificationsList.insertBefore(li, notificationsList.firstChild);
	li.innerHTML = notification.message;

	// Remove excess notifications
	// while(notificationsList.getElementByTagName('li').length > 5){
	// 	notificationsList.getElementByTagName("li")[5].remove();
	// }
}