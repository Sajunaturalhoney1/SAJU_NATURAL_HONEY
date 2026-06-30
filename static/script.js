/* ==========================================
   PRELOADER
========================================== */

window.addEventListener("load", () => {
    const preloader = document.getElementById("preloader");

    setTimeout(() => {
        preloader.style.opacity = "0";
        preloader.style.visibility = "hidden";
        preloader.style.transition = "0.8s";
    }, 1800);
});


/* ==========================================
   STICKY HEADER
========================================== */

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if(window.scrollY > 80){

        header.style.background="#ffffff";
        header.style.boxShadow="0 10px 25px rgba(0,0,0,.12)";
        header.style.padding="15px 8%";

    }

    else{

        header.style.background="rgba(255,255,255,.9)";
        header.style.boxShadow="0 5px 20px rgba(0,0,0,.08)";
        header.style.padding="18px 8%";

    }

});


/* ==========================================
   MOBILE MENU
========================================== */

const menu = document.querySelector(".menu");
const nav = document.querySelector("nav");

menu.addEventListener("click",()=>{

    nav.classList.toggle("show");

});


/* ==========================================
   COUNTER
========================================== */

const counters=document.querySelectorAll(".counter");

const counterObserver=new IntersectionObserver((entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

const counter=entry.target;

const target=+counter.getAttribute("data-target");

let current=0;

const speed=target/120;

const update=()=>{

current+=speed;

if(current<target){

counter.innerText=Math.floor(current);

requestAnimationFrame(update);

}

else{

counter.innerText=target+"+";

}

};

update();

counterObserver.unobserve(counter);

}

});

});

counters.forEach(counter=>{

counterObserver.observe(counter);

});


/* ==========================================
   SCROLL REVEAL
========================================== */

const reveals=document.querySelectorAll(
".section-title,.about-box,.why-card,.benefit,.product-card,.review-gallery img,.contact-container"
);

function revealAnimation(){

const windowHeight=window.innerHeight;

reveals.forEach(item=>{

const top=item.getBoundingClientRect().top;

if(top<windowHeight-120){

item.style.opacity="1";

item.style.transform="translateY(0)";

}

});

}

reveals.forEach(item=>{

item.style.opacity="0";

item.style.transform="translateY(80px)";
item.style.transition=".8s ease";

});

window.addEventListener("scroll",revealAnimation);

revealAnimation();


/* ==========================================
   PARTICLES RANDOM MOVEMENT
========================================== */

const particles=document.querySelectorAll(".particles span");

particles.forEach(particle=>{

particle.style.animationDuration=
(Math.random()*6+8)+"s";

particle.style.animationDelay=
(Math.random()*5)+"s";

particle.style.left=
(Math.random()*100)+"%";

});


/* ==========================================
   ACTIVE MENU
========================================== */

const sections=document.querySelectorAll("section");
const navLinks=document.querySelectorAll("nav a");

window.addEventListener("scroll",()=>{

let current="";

sections.forEach(section=>{

const sectionTop=section.offsetTop-120;

if(pageYOffset>=sectionTop){

current=section.getAttribute("id");

}

});

navLinks.forEach(link=>{

link.classList.remove("active");

if(link.getAttribute("href")==="#"+current){

link.classList.add("active");

}

});

});


/* ==========================================
   CONTACT FORM
========================================== */

const form = document.querySelector(".contact-form form");

if(form){

form.addEventListener("submit", () => {

alert("✅ Thank you for contacting SAJU Natural Honey.\n\nYour message has been sent successfully. We will contact you soon.");

});

}

/* ==========================================
   SMOOTH SCROLL
========================================== */

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

anchor.addEventListener("click",function(e){

e.preventDefault();

document.querySelector(this.getAttribute("href"))
.scrollIntoView({

behavior:"smooth"

});

});

});


/* ==========================================
   PRODUCT HOVER EFFECT
========================================== */

document.querySelectorAll(".product-card").forEach(card=>{

card.addEventListener("mousemove",(e)=>{

const rect=card.getBoundingClientRect();

const x=e.clientX-rect.left;
const y=e.clientY-rect.top;

card.style.transform=
`perspective(800px)
rotateX(${-(y-rect.height/2)/25}deg)
rotateY(${(x-rect.width/2)/25}deg)
translateY(-12px)`;

});

card.addEventListener("mouseleave",()=>{

card.style.transform="translateY(0px)";

});

});


/* ==========================================
   REVIEW IMAGE ZOOM
========================================== */

document.querySelectorAll(".review-gallery img").forEach(img=>{

img.addEventListener("click",()=>{

window.open(img.src,"_blank");

});

});


/* ==========================================
   FLOATING WHATSAPP PULSE
========================================== */

const whatsapp=document.querySelector(".floating-whatsapp");

setInterval(()=>{

whatsapp.animate([

{transform:"scale(1)"},

{transform:"scale(1.12)"},

{transform:"scale(1)"}

],{

duration:900

});

},2500);
