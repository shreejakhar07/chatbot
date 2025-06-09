import React from 'react';

const ProductCard = ({ product }) => {
  return (
    <div className="card mb-3">
      <img src={product.image_url} className="card-img-top" alt={product.name} />
      <div className="card-body">
        <h5 className="card-title">{product.name}</h5>
        <p>Brand: {product.brand}</p>
        <p>Category: {product.category}</p>
        <p>Price: ₹{product.price.toFixed(2)}</p>
      </div>
    </div>
  );
};

export default ProductCard;
