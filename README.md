Django Blog Project

Task 4 – Post Class-Based Views

This project implements a blog posts system using Django Class-Based Views.

Features

- Post list using "ListView"
- Pagination for posts
- Post details using "DetailView" with slug
- Create posts using "CreateView"
- Update posts using "UpdateView"
- Delete posts using "DeleteView"
- "LoginRequiredMixin" for authenticated actions
- "UserPassesTestMixin" to allow only post authors to edit or delete their posts
- "reverse_lazy" for success URLs
- Post templates inside "templates/posts/"
- Home page displays posts using "PostListView"

Post Fields

- Title
- Slug
- Body
- Created At
- Author

Templates

The post templates are located in:

"templates/posts/"

They include:

- "post_list.html"
- "post_detail.html"
- "post_form.html"
- "post_confirm_delete.html"