import { Component, output } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-register',
  imports: [ReactiveFormsModule],
  templateUrl: './register.html',
  styleUrl: './register.css',
})
export class Register {

  onToggleLogin = output();
  registerForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.registerForm = this.fb.group({
      nombre: ['', [Validators.required, Validators.maxLength(100)]],
      apellidos: ['', [Validators.required, Validators.maxLength(100)]],
      email: ['', [Validators.required, Validators.email, Validators.maxLength(100)]],
      edad: ['', [Validators.required, Validators.min(18)]],
      telefono: ['', [Validators.required, Validators.maxLength(100)]],
      direccion: ['', [Validators.required, Validators.maxLength(100)]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }

  onLoginClick() {
    this.onToggleLogin.emit();
  }

  onSubmit() {
    if (this.registerForm.valid) {
      const clienteData = this.registerForm.value;
      console.log('Datos del cliente:', clienteData);

      // Aquí harás la petición HTTP al backend Django
      // this.http.post('http://localhost:8000/api/clientes/', clienteData).subscribe(...)

    } else {
      console.log('Formulario inválido');
      // Marcar todos los campos como touched para mostrar errores
      Object.keys(this.registerForm.controls).forEach(key => {
        this.registerForm.get(key)?.markAsTouched();
      });
    }
  }

}
