document.getElementById('loanForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const form = e.target;
  const data = {
    gender: Number(form.gender.value),
    married: Number(form.married.value),
    education: Number(form.education.value),
    self_employed: Number(form.self_employed.value),
    total_income_log: Math.log(
      Number(form.applicant_income.value) + Number(form.coapplicant_income.value) + 1
    ),
    loan_amount: Number(form.loan_amount.value),
    loan_amount_term: Number(form.loan_amount_term.value),
    credit_history: Number(form.credit_history.value),
  };

  const res = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });

  const result = await res.json();
  document.getElementById('result').textContent =
    result.result === 'Approved' ? '✅ Loan Approved' : '❌ Loan Rejected';
});