var canvas = document.querySelector("canvas");

canvas.width = window.innerWidth / 2;
canvas.height = window.innerHeight / 2;
canvas.style.border = '1px solid black';

var context = canvas.getContext("2d");

var array = [];		// Creates an empty array

// Fills the array with numbers up to 10
for (let i = 0; i<10; i++) {
	var randint = Math.ceil(Math.random() * 10)
	if (!array.includes(randint)) {
		array.push(randint)
		context.fillRect(100 + i * 30, 200, 10, -array[i]*10)
	} else {
		i--
	}
}
// It is not very efficent, but good enough


var btn = document.createElement("BUTTON");
console.log(array)

var btn = document.createElement("BUTTON");   // Create a <button> element
btn.innerHTML = "Insertion Sort";                   // Insert text
document.body.appendChild(btn);               // Append <button> to <body>

btn.addEventListener("click", function() {
	insertion_sort(array);
})


function swap(array, pos_1, pos_2) {
	[array[pos_1], array[pos_2]] = [array[pos_2], array[pos_1]];
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function insertion_sort(array, pos=0) {
	if ((pos >= 0) && (pos < array.length)) {
		if (array[pos] > array[pos+1]) {
			swap(array, pos, pos+1);
			await sleep(500);
			context.clearRect(0, 0, canvas.width, canvas.height);
			for (var i = 0; i<10; i++) {
				if (i == pos) {
					context.fillStyle = "rgba(255, 0, 0, 1)"
				} else {
					context.fillStyle = "rgba(0, 0, 0, 1)"
				}
				context.fillRect(100 + i * 30, 200, 10, -array[i]*10)
			}
			await insertion_sort(array, pos-1);
		}
		await insertion_sort(array, pos+1);
	}
	console.log(array);
}

/*
context.fillStyle = "rgba(255, 0, 0, 0.5)"
context.fillRect(100, 100, 100, 100);

context.beginPath();
context.moveTo(50, 300);
context.lineTo(300, 100);
context.strokeStyle = "#fa34a3";
context.stroke();

function recursive_circle(x, y, radius, n) {
	if (n < 10) {
		context.beginPath();
		context.arc(x, y, radius, 0, Math.PI * 2, false);
		context.stroke();
		recursive_circle(x-radius, y+radius, radius/(n**(1/2)/2+1), n+1)
		recursive_circle(x+radius, y+radius, radius/(n**(1/2)/2+1), n+1)
	}
}

recursive_circle(300, 300, 60, 1)
*/