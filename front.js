videos = ["https://www.youtube.com/watch?v=WjQgsyPkuCk",,"https://www.youtube.com/watch?v=VFIGj5f8G1k"]
function changeBG(){ 

	 if (document.body.style.backgroundColor == 'lightblue') 
	 	document.body.style.backgroundColor = 'lightgray';
	 else
	 	document.body.style.backgroundColor = 'lightblue';


}
function playMusic(){
  var music = new Audio('song.mp3');
  music.play();
  }