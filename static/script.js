// Counters
let patientCount = 0;
let doctorCount = 0;
let appointmentCount = 0;

// DOM elements
const patientForm = document.querySelector("#patients form");
const doctorForm = document.querySelector("#doctors form");
const appointmentForm = document.querySelector("#appointments form");

const patientDisplay = document.querySelector("#dashboard .card:nth-child(1) p");
const doctorDisplay = document.querySelector("#dashboard .card:nth-child(2) p");
const appointmentDisplay = document.querySelector("#dashboard .card:nth-child(3) p");

// Update dashboard values
function updateDashboard() {
  patientDisplay.textContent = patientCount;
  doctorDisplay.textContent = doctorCount;
  appointmentDisplay.textContent = appointmentCount;
}

// Form event listeners
patientForm.addEventListener("submit", function (e) {
  e.preventDefault();
  patientCount++;
  updateDashboard();
  patientForm.reset();
});

doctorForm.addEventListener("submit", function (e) {
  e.preventDefault();
  doctorCount++;
  updateDashboard();
  doctorForm.reset();
});

appointmentForm.addEventListener("submit", function (e) {
  e.preventDefault();
  appointmentCount++;
  updateDashboard();
  appointmentForm.reset();
});
