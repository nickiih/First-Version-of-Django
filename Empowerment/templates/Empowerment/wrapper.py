<html>
<head>
</head>
<body>
  <h1>Add a New Product:</h1>
  <form method="POST" class="product-form"> {% csrf_token %}
    {{ form.non_field_errors }}
<div class="fieldWrapper">
  {{ form.First_Name.errors }}
  <label for="{{ form.subject.id_for_label }}">First Name:</label>
  <br>
  {{ form.First_Name }}<br>
</div>

<div class="fieldWrapper">
  {{ form.Last_Name.errors }}
  <label for="{{ form.subject.id_for_label }}">Last Name:</label>
  <br>
  {{ form.Last_Name }}
</div>

<div class="fieldWrapper">
  {{ form.Country.errors }}
  <label for="{{ form.subject.id_for_label }}">Country:</label>
  <br>
  {{ form.Country }}
</div>

<div class="fieldWrapper">
  {{ form.Product.errors }}
  <label for="{{ form.subject.id_for_label }}">Product:</label>
  <br>
  {{ form.Product }}
</div>

<div class="fieldWrapper">
  {{ form.Product_Description.errors }}
  <label for="{{ form.subject.id_for_label }}">Product Description:</label>
  <br>
  {{ form.Product_Description }}
</div>

      <button type="submit" class="save btn btn-default">Save</button>
  </form>
</body>
</html>
