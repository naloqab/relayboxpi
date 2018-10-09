
/* var backgrounds = ['cat.jpg', 'cat2.jpg', 'cat3.jpg'];

var background = backgrounds[Math.floor(Math.random() * backgrounds.length)];

var background = "url(../images/"+background+")";

$(document).ready(function(){
	$('body').css({'background':background, 'background-repeat': 'no-repeat'});
}); */

UpdateButtons();
setTimeout(function() {
	BedroomButtonUpdateState();
	LivingRoomButtonUpdateState();
	AllButtonUpdateState();
}, 1000);

setInterval(function()
{
	UpdateButtons();
	setTimeout(function() {
		BedroomButtonUpdateState();
		LivingRoomButtonUpdateState();
		AllButtonUpdateState();
	}, 1000);

}, 20000);

function UpdateButtons()
{
	$.ajax
	({
		url: "GetStatusUpdate.php", 
		success: (function (result)
		{
			$("#UpdateButtonsData").empty().append(result);

			if (R1 == 'ON')
			{
				$("#Relay1").prop('checked', true);
			}
			else
			{
				$("#Relay1").prop('checked', false);
			}

			if (R2 == 'ON')
			{
				$("#Relay2").prop('checked', true);
			}
			else
			{
				$("#Relay2").prop('checked', false);
			}

			if (R3 == 'ON')
			{
				$("#Relay3").prop('checked', true);
			}
			else
			{
				$("#Relay3").prop('checked', false);
			}

			if (R4 == 'ON')
			{
				$("#Relay4").prop('checked', true);
			}
			else
			{
				$("#Relay4").prop('checked', false);
			}

			// if (L == 'Locked')
			// {
			// 	$("#DoorLock").prop('checked', false);
			// }
			// else
			// {
			// 	$("#DoorLock").prop('checked', true);
			// }

			if (GPC == 'ON')
			{
				$("#GamingPC").prop('checked', true);
			}
			else
			{
				$("#GamingPC").prop('checked', false);
			}
		})
	})
};

function GamingPCPower()
{
	if ( $("#GamingPC").prop('checked'))
	{
		$.get("GamingPCPower.php?Power=ON");
	}
	else
	{
		$.get("GamingPCPower.php?Power=OFF");
	}
}

function DoorLockStatus()
{
	if ( $("#DoorLock").prop('checked'))
	{
		$.get("UnlockDoor.php");
	}
	else
	{
		$.get("LockDoor.php");
	}
}

function BedroomButtonUpdateState()
{
	if ( $("#Relay3").prop('checked') || $("#Relay4").prop('checked') )
	{
		$("#Bedroom").prop('checked', true);
	}

	if ( $("#Relay3").prop('checked') == false && $("#Relay4").prop('checked') == false)	
	{
		$("#Bedroom").prop('checked', false);
	}
}

function LivingRoomButtonUpdateState()
{
	if ( $("#Relay1").prop('checked') || $("#Relay2").prop('checked') )
	{
		$("#LivingRoom").prop('checked', true);
	}

	if ( $("#Relay1").prop('checked') == false && $("#Relay2").prop('checked') == false)
	{
		$("#LivingRoom").prop('checked', false);
	}
}

function AllButtonUpdateState()
{
	if ( $("#Bedroom").prop('checked') || $("#LivingRoom").prop('checked') )
	{
		$("#AllRelays").prop('checked', true);
	}

	if ( $("#Bedroom").prop('checked') == false && $("#LivingRoom").prop('checked') == false)
	{
		$("#AllRelays").prop('checked', false);
	}
}

function AllBedroom()
{
	if ( $("#Bedroom").prop('checked') )
	{
		$("#Relay3").prop('checked', true);
		$("#Relay4").prop('checked', true);
	}

	else
	{
		$("#Relay3").prop('checked', false);
		$("#Relay4").prop('checked', false);
	}
	
	RelayStatusChange($("#Relay3"));
	RelayStatusChange($("#Relay4"));
	
	AllButtonUpdateState();
}

function AllLivingRoom()
{
	if ( $("#LivingRoom").prop('checked') )
	{
		$("#Relay1").prop('checked', true);
		$("#Relay2").prop('checked', true);
	}

	else
	{
		$("#Relay1").prop('checked', false);
		$("#Relay2").prop('checked', false);
	}
	
	RelayStatusChange($("#Relay1"));
	RelayStatusChange($("#Relay2"));
	
	AllButtonUpdateState();
}

function All()
{
	if ( $("#AllRelays").prop('checked') )
	{
		$.get("Relay.php?RelayNumber=All&RelayStatus=ON");
		$("#Relay1").prop('checked', true);
		$("#Relay2").prop('checked', true);
		$("#Relay3").prop('checked', true);
		$("#Relay4").prop('checked', true);
	}

	else
	{
		$.get("Relay.php?RelayNumber=All&RelayStatus=OFF");
		$("#Relay1").prop('checked', false);
		$("#Relay2").prop('checked', false);
		$("#Relay3").prop('checked', false);
		$("#Relay4").prop('checked', false);
	}

	LivingRoomButtonUpdateState();
	BedroomButtonUpdateState();
}

function RelayStatusChange(element)
{
	var RelayNumber = $(element).attr("value");
	var RelayID = $(element).attr("id");
	
	if ( $('#'+RelayID).prop('checked') )
	{
		$.get("Relay.php?RelayNumber="+RelayNumber+"&RelayStatus=ON");
	}
	else
	{
		$.get("Relay.php?RelayNumber="+RelayNumber+"&RelayStatus=OFF");
	}

	LivingRoomButtonUpdateState();
	BedroomButtonUpdateState();
	AllButtonUpdateState();
}
