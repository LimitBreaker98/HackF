import { Component, ɵbypassSanitizationTrustResourceUrl } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  readonly ROOT_URL = 'https://jsonplaceholder.typicode.com';

  constructor(private http: HttpClient, private router: Router){}

  title = 'front';

  isHomeRoute() {
    return this.router.url === '/';
  }

  isChecked()
  {
    let email = document.getElementById("exampleInputPassword1");
    let pass = document.getElementById("exampleInputEmail1")
    return email == null && pass == null;
  }

  validate(){
    return true;
  }

  ngOnInit(){
  }
  
}
