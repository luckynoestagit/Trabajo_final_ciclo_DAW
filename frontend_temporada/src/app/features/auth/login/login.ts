import { Component, output } from '@angular/core';

@Component({
  selector: 'app-login',
  imports: [],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {

  onToggleRegister = output();

  onRegisterClick() {
    this.onToggleRegister.emit();
  }

}
