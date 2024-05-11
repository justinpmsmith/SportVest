export const config = {
  apiUrl: `http://${process.env.DOCKER_HOSTNAME_INTERNAL}:8000`,
  sellSomethingExt: "/backend/submit-form/",
  loadProductsExt: "/backend/products",
  soldItemsExt: "/backend/sold-items/",
  contactUsExt: "/backend/contact-us/",
};
