# To install rust and dependencies for testing simple MPI application
https://github.com/rsmpi/rsmpi


## MacOS
```
brew install autoconf automake libtool
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Test Install on MacOS
```
cargo new testmpi
echo "mpi = \"0.5.4\"">>Cargo.toml
cargo build
```

=====
Not supported (yet):
- One-sided communication (RMA)

=====
Gives Error.

error[E0425]: cannot find function, tuple struct or tuple variant `MPI_Type_hvector` in module `ffi`
    --> /Users/niall/.cargo/registry/src/github.com-1ecc6299db9ec823/mpi-0.5.4/src/datatype.rs:212:18
     |
212  |             ffi::MPI_Type_hvector(count, blocklength, stride, oldtype.as_raw(), &mut newtype);
     |                  ^^^^^^^^^^^^^^^^ help: a function with a similar name exists: `MPI_Type_vector`
     |
    ::: /Users/niall/Workspace/Rust/tdLBRust/target/debug/build/mpi-sys-636c08e7a572828e/out/functions_and_types.rs:1304:2
     |
1304 |  pub fn MPI_Type_vector ( count : :: std :: os :: raw :: c_int , blocklength : :: std :: os :: raw :: c_int , stride : :: std :: os :: raw :: c_int , oldtype : MPI_Datatype , newtype : * mut MPI_Datatype , ) -> :: std :: os :: raw :: c_int ;
     |  ----------------------------------------------------------------------------------------------------------------------------------------------------[package]
-------------------------------------------------------------------------------------------- similarly named function `MPI_Type_vector` defined here

error: aborting due to previous error

For more information about this error, try `rustc --explain E0425`.
error: could not compile `mpi`.


