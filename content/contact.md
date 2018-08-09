+++
title = "Contact"
weight = 40
draft = false
+++

Thanks for stopping by! This means we're friends now, right?   
Feel free to drop me a line! My other social media homes are in the icons below.

<form class="contact-form" id="contact-form" method="post">
	<div class="field half first">
		<label for="name">Name</label>
		<input type="text" name="name" id="name" />
	</div>
	<div class="field half">
		<label for="email">Email</label>
		<input type="text" name="email" id="email" />
	</div>
	<div class="field">
		<label for="message">Message</label>
		<textarea name="message" id="message" rows="4"></textarea>
	</div>
	<ul class="actions">
		<li><button type="button" onClick="submitToAPI(event)" class="btn btn-lg" style="margin-top:20px;">Submit</button></li>
		<li><button type="reset" value="reset"class="btn btn-lg" style="margin-top:20px;">Reset</button></li>
	</ul>
</form>

{{< socialLinks >}}
