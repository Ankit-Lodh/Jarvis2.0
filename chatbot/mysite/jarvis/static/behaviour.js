const socket = new WebSocket('ws://localhost:8000/ws/jarvis/')
var playAnnimation1 = document.getElementById("circle1").animate([
  {transform:'scale(1,1)',opacity:'0.5'},
  {transform: 'scale(3.5,3.5)',opacity:'0'}
],
{
  duration: 4000,
  iterations: Infinity
});
var playAnnimation2 = document.getElementById("circle2").animate([
  {transform:'scale(1,1)',opacity:'0.5'},
  {transform: 'scale(3.5,3.5)',opacity:'0'}
],
{
  duration: 5000,
  iterations: Infinity
});
var playAnnimation3 = document.getElementById("circle3").animate([
  {transform:'scale(1,1)',opacity:'0.5'},
  {transform: 'scale(3.5,3.5)',opacity:'0'}
],
{
  duration: 6000,
  iterations: Infinity
});
var playAnnimation4 = document.getElementById("circle4").animate([
  {transform:'scale(1,1)',opacity:'0.5'},
  {transform: 'scale(3.5,3.5)',opacity:'0'}
],
{
  duration: 7000,
  iterations: Infinity
});
var speech = true;
window.SpeechRecognition = window.SpeechRecognition
        || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = true;
const words = document.querySelector('.words');
words.appendChild(p);

recognition.addEventListener('result', e => {
  let text_val = document.getElementById("answer").innerHTML
  
  if (text_val.length === 0){
      playAnnimation1.cancel();
      playAnnimation2.cancel();
      playAnnimation3.cancel();
      playAnnimation4.cancel();
      console.log(e.results[0][0].transcript)
      document.getElementById("p").innerHTML = e.results[0][0].transcript;
      document.getElementById("p").style.color = "red"; 
      console.log(3)
  }
  // this line of code to change the color/style at the time speech to text convertion
});
if (speech == true) {
  recognition.start();
  recognition.addEventListener('end', recognition.start);
  recognition.onaudioend = function() {
    socket.onopen = setTimeout(function (event) {
        socket.send(document.getElementById("p").innerHTML);
        document.getElementById("p").innerHTML = "";
        },1000)
}
}
socket.onmessage = function (event) {
  document.getElementById("answer").innerHTML = event.data
  let utterance = new SpeechSynthesisUtterance(event.data);
 // to speak what ever data come out from server
  speechSynthesis.speak(utterance);
  playAnnimation1.play();
  playAnnimation2.play();
  playAnnimation3.play();
  playAnnimation4.play();
  console.log(11)
  setTimeout(function(){ 
  document.getElementById("answer").innerHTML = ""; }, 8000);
  console.log(event.data)
  }
socket.onclose = function(e){
  alert('Connection CLosed');
};