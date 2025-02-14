const openMenuBtn = document.querySelector('#openMenuBtn');
const closeMenuBtn = document.querySelector('#closeMenuBtn');
const menu = document.querySelector('#menu');

openMenuBtn.addEventListener('click', () => {
  handleViewTransition(openMenu);
});

closeMenuBtn.addEventListener('click', () => {
  handleViewTransition(closeMenu);
});

// Close menu by Press Escape(ESC)
function handleCloseWithESC(e) {
  if (e.key == 'Escape') {
    handleViewTransition(closeMenu);
  }
}

function openMenu() {
  menu.classList.add('open');
  closeMenuBtn.focus();
  window.addEventListener('keyup', handleCloseWithESC);
}

function closeMenu() {
  menu.classList.remove('open');
  openMenuBtn.focus();
  window.removeEventListener('keyup', handleCloseWithESC);
}

function handleViewTransition(updateDom) {
  if (!document.startViewTransition) updateDom();
  else document.startViewTransition(() => updateDom());
}

document.querySelectorAll('.NavLink').forEach((link) => {
  link.addEventListener('click', () => handleViewTransition(closeMenu));
});

//  Scroll Animation

let scrollDirection;
const nav = document.querySelector('.Navbar');
document.addEventListener(
  'scroll',
  (e) => {
    const st = window.pageYOffset || document.documentElement.scrollTop;
    const direction = st > e.target.lastScrollTop ? 'down' : 'up';
    if (Math.abs(st - e.target.lastScrollTop) > 5)
      document.body.setAttribute('scroll-direction', direction);
    scrollDirection = direction;
    e.target.lastScrollTop = st <= 0 ? 0 : st;
  },
  {
    passive: true,
  }
);

function addRevealEffect(elements) {
  const observer = new IntersectionObserver(
    (entries) => {
      let revealClass;
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          revealClass = scrollDirection === 'up' ? 'reveal-up' : 'reveal-down';

          entry.target.classList.add(revealClass);
        } else {
          entry.target.className = 'subject';
        }
      });
    },
    { threshold: 0.1 }
  );

  elements.forEach((element) => {
    observer.observe(element);
  });
}

const elementsToReveal = document.querySelectorAll('.subject');
addRevealEffect(elementsToReveal);

//  About Text Replace

const NORMAL_PLAYBACK_RATE = 200;
const REDUCED_PLAYBACK_RATE = 1000;

let rate = NORMAL_PLAYBACK_RATE;

const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
if (mediaQuery.matches) rate = REDUCED_PLAYBACK_RATE;

const words = [
  'passion',
  'success',
  'goals',
  'rhythm',
  'fun',
  'energy',
  'opportunity',
];

textReplace(words, 'target-word', rate);

function textReplace(words, targetElement, rate) {
  let wordIndex = 0;

  const randomWordElement = document.getElementById(targetElement);

  const changeWordWithAnimation = () => {
    randomWordElement.style.opacity = 0; // Fade out
    setTimeout(function () {
      wordIndex = (wordIndex + 1) % words.length;
      randomWordElement.textContent = words[wordIndex];
      randomWordElement.style.opacity = 1; // Fade in
    }, 50);
  };

  const interval = setInterval(changeWordWithAnimation, rate);
}

/* // PayPal Button Configuration
paypal.Buttons({
    createOrder: function(data, actions) {
        // This function sets up the details of the transaction
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: '29.99'  // Replace with your product price
                },
                description: "Natural Soap Product"
            }]
        });
    },
    onApprove: function(data, actions) {
        // This function captures the funds from the transaction
        return actions.order.capture().then(function(details) {
            // Show a success message to your buyer
            alert('Transaction completed by ' + details.payer.name.given_name);
            // Call your server to save the transaction
            return fetch('/create-payment/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    orderID: data.orderID,
                    payerID: data.payerID,
                    paymentID: details.id
                })
            });
        });
    },
    onError: function(err) {
        console.error('Payment Error:', err);
        alert('There was an error processing your payment');
    }
}).render('#paypal-button-container');

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} */