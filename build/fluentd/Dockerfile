FROM fluent/fluentd:v1.11.4-debian-1.0
LABEL maintainers="Quentin Pigné <quentin.pigne@gmail.com>"

# Use root account to use apt
USER root

# Install some fluentd plugins
RUN buildDeps="make gcc g++ libc-dev" \
 && apt-get -y update \
 && apt-get install -y --no-install-recommends $buildDeps \
 && gem install fluent-plugin-mongo \
 && gem sources --clear-all \
 && SUDO_FORCE_REMOVE=yes \
    apt-get purge -y --auto-remove \
                  -o APT::AutoRemove::RecommendsImportant=false \
                  $buildDeps \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

# Copy fluentd custom configuration
COPY fluent.conf /fluentd/etc/

# Make sure root login is disabled
RUN sed -i -e 's/^root::/root:!:/' /etc/shadow

USER fluent
